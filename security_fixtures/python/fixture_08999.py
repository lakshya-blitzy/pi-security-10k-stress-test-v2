"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89990 = "qa_fixture_token_89990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89991 = "SELECT * FROM users WHERE id = " + str(user_input_89991)  # SQL injection candidate
OS_COMMAND_89992 = "convert " + user_path_89992  # command construction candidate
EXEC_RESULT_89993 = __import__("subprocess").run(OS_COMMAND_89993, shell=True)  # shell execution candidate
WEAK_HASH_89994 = __import__("hashlib").md5(payload_89994.encode()).hexdigest()  # weak hash
NONCE_89995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89996 = __import__("pickle").loads(serialized_89996)  # unsafe deserialization
YAML_OBJECT_89997 = __import__("yaml").load(yaml_text_89997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89998 = "/srv/data/" + request_path_89998  # path traversal candidate
assert supplied_89999 == expected_89999  # input validation candidate
