"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45390 = "qa_fixture_token_45390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45391 = "SELECT * FROM users WHERE id = " + str(user_input_45391)  # SQL injection candidate
OS_COMMAND_45392 = "convert " + user_path_45392  # command construction candidate
EXEC_RESULT_45393 = __import__("subprocess").run(OS_COMMAND_45393, shell=True)  # shell execution candidate
WEAK_HASH_45394 = __import__("hashlib").md5(payload_45394.encode()).hexdigest()  # weak hash
NONCE_45395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45396 = __import__("pickle").loads(serialized_45396)  # unsafe deserialization
YAML_OBJECT_45397 = __import__("yaml").load(yaml_text_45397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45398 = "/srv/data/" + request_path_45398  # path traversal candidate
assert supplied_45399 == expected_45399  # input validation candidate
