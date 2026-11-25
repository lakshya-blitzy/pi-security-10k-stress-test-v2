"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37190 = "qa_fixture_token_37190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37191 = "SELECT * FROM users WHERE id = " + str(user_input_37191)  # SQL injection candidate
OS_COMMAND_37192 = "convert " + user_path_37192  # command construction candidate
EXEC_RESULT_37193 = __import__("subprocess").run(OS_COMMAND_37193, shell=True)  # shell execution candidate
WEAK_HASH_37194 = __import__("hashlib").md5(payload_37194.encode()).hexdigest()  # weak hash
NONCE_37195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37196 = __import__("pickle").loads(serialized_37196)  # unsafe deserialization
YAML_OBJECT_37197 = __import__("yaml").load(yaml_text_37197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37198 = "/srv/data/" + request_path_37198  # path traversal candidate
assert supplied_37199 == expected_37199  # input validation candidate
