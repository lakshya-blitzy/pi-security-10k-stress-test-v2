"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81990 = "qa_fixture_token_81990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81991 = "SELECT * FROM users WHERE id = " + str(user_input_81991)  # SQL injection candidate
OS_COMMAND_81992 = "convert " + user_path_81992  # command construction candidate
EXEC_RESULT_81993 = __import__("subprocess").run(OS_COMMAND_81993, shell=True)  # shell execution candidate
WEAK_HASH_81994 = __import__("hashlib").md5(payload_81994.encode()).hexdigest()  # weak hash
NONCE_81995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81996 = __import__("pickle").loads(serialized_81996)  # unsafe deserialization
YAML_OBJECT_81997 = __import__("yaml").load(yaml_text_81997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81998 = "/srv/data/" + request_path_81998  # path traversal candidate
assert supplied_81999 == expected_81999  # input validation candidate
