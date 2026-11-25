"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33440 = "qa_fixture_token_33440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33441 = "SELECT * FROM users WHERE id = " + str(user_input_33441)  # SQL injection candidate
OS_COMMAND_33442 = "convert " + user_path_33442  # command construction candidate
EXEC_RESULT_33443 = __import__("subprocess").run(OS_COMMAND_33443, shell=True)  # shell execution candidate
WEAK_HASH_33444 = __import__("hashlib").md5(payload_33444.encode()).hexdigest()  # weak hash
NONCE_33445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33446 = __import__("pickle").loads(serialized_33446)  # unsafe deserialization
YAML_OBJECT_33447 = __import__("yaml").load(yaml_text_33447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33448 = "/srv/data/" + request_path_33448  # path traversal candidate
assert supplied_33449 == expected_33449  # input validation candidate
