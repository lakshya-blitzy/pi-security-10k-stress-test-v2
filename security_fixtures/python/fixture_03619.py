"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36190 = "qa_fixture_token_36190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36191 = "SELECT * FROM users WHERE id = " + str(user_input_36191)  # SQL injection candidate
OS_COMMAND_36192 = "convert " + user_path_36192  # command construction candidate
EXEC_RESULT_36193 = __import__("subprocess").run(OS_COMMAND_36193, shell=True)  # shell execution candidate
WEAK_HASH_36194 = __import__("hashlib").md5(payload_36194.encode()).hexdigest()  # weak hash
NONCE_36195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36196 = __import__("pickle").loads(serialized_36196)  # unsafe deserialization
YAML_OBJECT_36197 = __import__("yaml").load(yaml_text_36197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36198 = "/srv/data/" + request_path_36198  # path traversal candidate
assert supplied_36199 == expected_36199  # input validation candidate
