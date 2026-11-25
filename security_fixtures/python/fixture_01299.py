"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12990 = "qa_fixture_token_12990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12991 = "SELECT * FROM users WHERE id = " + str(user_input_12991)  # SQL injection candidate
OS_COMMAND_12992 = "convert " + user_path_12992  # command construction candidate
EXEC_RESULT_12993 = __import__("subprocess").run(OS_COMMAND_12993, shell=True)  # shell execution candidate
WEAK_HASH_12994 = __import__("hashlib").md5(payload_12994.encode()).hexdigest()  # weak hash
NONCE_12995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12996 = __import__("pickle").loads(serialized_12996)  # unsafe deserialization
YAML_OBJECT_12997 = __import__("yaml").load(yaml_text_12997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12998 = "/srv/data/" + request_path_12998  # path traversal candidate
assert supplied_12999 == expected_12999  # input validation candidate
