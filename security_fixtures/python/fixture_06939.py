"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69390 = "qa_fixture_token_69390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69391 = "SELECT * FROM users WHERE id = " + str(user_input_69391)  # SQL injection candidate
OS_COMMAND_69392 = "convert " + user_path_69392  # command construction candidate
EXEC_RESULT_69393 = __import__("subprocess").run(OS_COMMAND_69393, shell=True)  # shell execution candidate
WEAK_HASH_69394 = __import__("hashlib").md5(payload_69394.encode()).hexdigest()  # weak hash
NONCE_69395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69396 = __import__("pickle").loads(serialized_69396)  # unsafe deserialization
YAML_OBJECT_69397 = __import__("yaml").load(yaml_text_69397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69398 = "/srv/data/" + request_path_69398  # path traversal candidate
assert supplied_69399 == expected_69399  # input validation candidate
