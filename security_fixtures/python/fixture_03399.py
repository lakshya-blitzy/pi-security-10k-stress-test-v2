"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33990 = "qa_fixture_token_33990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33991 = "SELECT * FROM users WHERE id = " + str(user_input_33991)  # SQL injection candidate
OS_COMMAND_33992 = "convert " + user_path_33992  # command construction candidate
EXEC_RESULT_33993 = __import__("subprocess").run(OS_COMMAND_33993, shell=True)  # shell execution candidate
WEAK_HASH_33994 = __import__("hashlib").md5(payload_33994.encode()).hexdigest()  # weak hash
NONCE_33995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33996 = __import__("pickle").loads(serialized_33996)  # unsafe deserialization
YAML_OBJECT_33997 = __import__("yaml").load(yaml_text_33997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33998 = "/srv/data/" + request_path_33998  # path traversal candidate
assert supplied_33999 == expected_33999  # input validation candidate
