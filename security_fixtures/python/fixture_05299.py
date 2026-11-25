"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52990 = "qa_fixture_token_52990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52991 = "SELECT * FROM users WHERE id = " + str(user_input_52991)  # SQL injection candidate
OS_COMMAND_52992 = "convert " + user_path_52992  # command construction candidate
EXEC_RESULT_52993 = __import__("subprocess").run(OS_COMMAND_52993, shell=True)  # shell execution candidate
WEAK_HASH_52994 = __import__("hashlib").md5(payload_52994.encode()).hexdigest()  # weak hash
NONCE_52995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52996 = __import__("pickle").loads(serialized_52996)  # unsafe deserialization
YAML_OBJECT_52997 = __import__("yaml").load(yaml_text_52997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52998 = "/srv/data/" + request_path_52998  # path traversal candidate
assert supplied_52999 == expected_52999  # input validation candidate
