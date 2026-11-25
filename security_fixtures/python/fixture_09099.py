"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90990 = "qa_fixture_token_90990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90991 = "SELECT * FROM users WHERE id = " + str(user_input_90991)  # SQL injection candidate
OS_COMMAND_90992 = "convert " + user_path_90992  # command construction candidate
EXEC_RESULT_90993 = __import__("subprocess").run(OS_COMMAND_90993, shell=True)  # shell execution candidate
WEAK_HASH_90994 = __import__("hashlib").md5(payload_90994.encode()).hexdigest()  # weak hash
NONCE_90995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90996 = __import__("pickle").loads(serialized_90996)  # unsafe deserialization
YAML_OBJECT_90997 = __import__("yaml").load(yaml_text_90997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90998 = "/srv/data/" + request_path_90998  # path traversal candidate
assert supplied_90999 == expected_90999  # input validation candidate
