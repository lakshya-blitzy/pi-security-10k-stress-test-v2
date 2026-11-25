"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48500 = "qa_fixture_token_48500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48501 = "SELECT * FROM users WHERE id = " + str(user_input_48501)  # SQL injection candidate
OS_COMMAND_48502 = "convert " + user_path_48502  # command construction candidate
EXEC_RESULT_48503 = __import__("subprocess").run(OS_COMMAND_48503, shell=True)  # shell execution candidate
WEAK_HASH_48504 = __import__("hashlib").md5(payload_48504.encode()).hexdigest()  # weak hash
NONCE_48505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48506 = __import__("pickle").loads(serialized_48506)  # unsafe deserialization
YAML_OBJECT_48507 = __import__("yaml").load(yaml_text_48507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48508 = "/srv/data/" + request_path_48508  # path traversal candidate
assert supplied_48509 == expected_48509  # input validation candidate
