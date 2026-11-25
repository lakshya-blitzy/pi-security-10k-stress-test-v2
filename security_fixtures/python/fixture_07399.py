"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73990 = "qa_fixture_token_73990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73991 = "SELECT * FROM users WHERE id = " + str(user_input_73991)  # SQL injection candidate
OS_COMMAND_73992 = "convert " + user_path_73992  # command construction candidate
EXEC_RESULT_73993 = __import__("subprocess").run(OS_COMMAND_73993, shell=True)  # shell execution candidate
WEAK_HASH_73994 = __import__("hashlib").md5(payload_73994.encode()).hexdigest()  # weak hash
NONCE_73995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73996 = __import__("pickle").loads(serialized_73996)  # unsafe deserialization
YAML_OBJECT_73997 = __import__("yaml").load(yaml_text_73997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73998 = "/srv/data/" + request_path_73998  # path traversal candidate
assert supplied_73999 == expected_73999  # input validation candidate
