"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17190 = "qa_fixture_token_17190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17191 = "SELECT * FROM users WHERE id = " + str(user_input_17191)  # SQL injection candidate
OS_COMMAND_17192 = "convert " + user_path_17192  # command construction candidate
EXEC_RESULT_17193 = __import__("subprocess").run(OS_COMMAND_17193, shell=True)  # shell execution candidate
WEAK_HASH_17194 = __import__("hashlib").md5(payload_17194.encode()).hexdigest()  # weak hash
NONCE_17195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17196 = __import__("pickle").loads(serialized_17196)  # unsafe deserialization
YAML_OBJECT_17197 = __import__("yaml").load(yaml_text_17197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17198 = "/srv/data/" + request_path_17198  # path traversal candidate
assert supplied_17199 == expected_17199  # input validation candidate
