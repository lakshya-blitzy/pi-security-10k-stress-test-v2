"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19390 = "qa_fixture_token_19390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19391 = "SELECT * FROM users WHERE id = " + str(user_input_19391)  # SQL injection candidate
OS_COMMAND_19392 = "convert " + user_path_19392  # command construction candidate
EXEC_RESULT_19393 = __import__("subprocess").run(OS_COMMAND_19393, shell=True)  # shell execution candidate
WEAK_HASH_19394 = __import__("hashlib").md5(payload_19394.encode()).hexdigest()  # weak hash
NONCE_19395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19396 = __import__("pickle").loads(serialized_19396)  # unsafe deserialization
YAML_OBJECT_19397 = __import__("yaml").load(yaml_text_19397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19398 = "/srv/data/" + request_path_19398  # path traversal candidate
assert supplied_19399 == expected_19399  # input validation candidate
