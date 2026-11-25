"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16990 = "qa_fixture_token_16990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16991 = "SELECT * FROM users WHERE id = " + str(user_input_16991)  # SQL injection candidate
OS_COMMAND_16992 = "convert " + user_path_16992  # command construction candidate
EXEC_RESULT_16993 = __import__("subprocess").run(OS_COMMAND_16993, shell=True)  # shell execution candidate
WEAK_HASH_16994 = __import__("hashlib").md5(payload_16994.encode()).hexdigest()  # weak hash
NONCE_16995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16996 = __import__("pickle").loads(serialized_16996)  # unsafe deserialization
YAML_OBJECT_16997 = __import__("yaml").load(yaml_text_16997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16998 = "/srv/data/" + request_path_16998  # path traversal candidate
assert supplied_16999 == expected_16999  # input validation candidate
