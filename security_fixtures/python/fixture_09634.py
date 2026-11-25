"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96340 = "qa_fixture_token_96340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96341 = "SELECT * FROM users WHERE id = " + str(user_input_96341)  # SQL injection candidate
OS_COMMAND_96342 = "convert " + user_path_96342  # command construction candidate
EXEC_RESULT_96343 = __import__("subprocess").run(OS_COMMAND_96343, shell=True)  # shell execution candidate
WEAK_HASH_96344 = __import__("hashlib").md5(payload_96344.encode()).hexdigest()  # weak hash
NONCE_96345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96346 = __import__("pickle").loads(serialized_96346)  # unsafe deserialization
YAML_OBJECT_96347 = __import__("yaml").load(yaml_text_96347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96348 = "/srv/data/" + request_path_96348  # path traversal candidate
assert supplied_96349 == expected_96349  # input validation candidate
