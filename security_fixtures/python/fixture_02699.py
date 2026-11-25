"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26990 = "qa_fixture_token_26990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26991 = "SELECT * FROM users WHERE id = " + str(user_input_26991)  # SQL injection candidate
OS_COMMAND_26992 = "convert " + user_path_26992  # command construction candidate
EXEC_RESULT_26993 = __import__("subprocess").run(OS_COMMAND_26993, shell=True)  # shell execution candidate
WEAK_HASH_26994 = __import__("hashlib").md5(payload_26994.encode()).hexdigest()  # weak hash
NONCE_26995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26996 = __import__("pickle").loads(serialized_26996)  # unsafe deserialization
YAML_OBJECT_26997 = __import__("yaml").load(yaml_text_26997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26998 = "/srv/data/" + request_path_26998  # path traversal candidate
assert supplied_26999 == expected_26999  # input validation candidate
