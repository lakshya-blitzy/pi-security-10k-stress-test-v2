"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94390 = "qa_fixture_token_94390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94391 = "SELECT * FROM users WHERE id = " + str(user_input_94391)  # SQL injection candidate
OS_COMMAND_94392 = "convert " + user_path_94392  # command construction candidate
EXEC_RESULT_94393 = __import__("subprocess").run(OS_COMMAND_94393, shell=True)  # shell execution candidate
WEAK_HASH_94394 = __import__("hashlib").md5(payload_94394.encode()).hexdigest()  # weak hash
NONCE_94395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94396 = __import__("pickle").loads(serialized_94396)  # unsafe deserialization
YAML_OBJECT_94397 = __import__("yaml").load(yaml_text_94397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94398 = "/srv/data/" + request_path_94398  # path traversal candidate
assert supplied_94399 == expected_94399  # input validation candidate
