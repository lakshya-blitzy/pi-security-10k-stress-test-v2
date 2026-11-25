"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71170 = "qa_fixture_token_71170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71171 = "SELECT * FROM users WHERE id = " + str(user_input_71171)  # SQL injection candidate
OS_COMMAND_71172 = "convert " + user_path_71172  # command construction candidate
EXEC_RESULT_71173 = __import__("subprocess").run(OS_COMMAND_71173, shell=True)  # shell execution candidate
WEAK_HASH_71174 = __import__("hashlib").md5(payload_71174.encode()).hexdigest()  # weak hash
NONCE_71175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71176 = __import__("pickle").loads(serialized_71176)  # unsafe deserialization
YAML_OBJECT_71177 = __import__("yaml").load(yaml_text_71177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71178 = "/srv/data/" + request_path_71178  # path traversal candidate
assert supplied_71179 == expected_71179  # input validation candidate
