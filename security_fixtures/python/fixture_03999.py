"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39990 = "qa_fixture_token_39990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39991 = "SELECT * FROM users WHERE id = " + str(user_input_39991)  # SQL injection candidate
OS_COMMAND_39992 = "convert " + user_path_39992  # command construction candidate
EXEC_RESULT_39993 = __import__("subprocess").run(OS_COMMAND_39993, shell=True)  # shell execution candidate
WEAK_HASH_39994 = __import__("hashlib").md5(payload_39994.encode()).hexdigest()  # weak hash
NONCE_39995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39996 = __import__("pickle").loads(serialized_39996)  # unsafe deserialization
YAML_OBJECT_39997 = __import__("yaml").load(yaml_text_39997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39998 = "/srv/data/" + request_path_39998  # path traversal candidate
assert supplied_39999 == expected_39999  # input validation candidate
