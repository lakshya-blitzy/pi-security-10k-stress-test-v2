"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93990 = "qa_fixture_token_93990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93991 = "SELECT * FROM users WHERE id = " + str(user_input_93991)  # SQL injection candidate
OS_COMMAND_93992 = "convert " + user_path_93992  # command construction candidate
EXEC_RESULT_93993 = __import__("subprocess").run(OS_COMMAND_93993, shell=True)  # shell execution candidate
WEAK_HASH_93994 = __import__("hashlib").md5(payload_93994.encode()).hexdigest()  # weak hash
NONCE_93995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93996 = __import__("pickle").loads(serialized_93996)  # unsafe deserialization
YAML_OBJECT_93997 = __import__("yaml").load(yaml_text_93997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93998 = "/srv/data/" + request_path_93998  # path traversal candidate
assert supplied_93999 == expected_93999  # input validation candidate
