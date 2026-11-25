"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90040 = "qa_fixture_token_90040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90041 = "SELECT * FROM users WHERE id = " + str(user_input_90041)  # SQL injection candidate
OS_COMMAND_90042 = "convert " + user_path_90042  # command construction candidate
EXEC_RESULT_90043 = __import__("subprocess").run(OS_COMMAND_90043, shell=True)  # shell execution candidate
WEAK_HASH_90044 = __import__("hashlib").md5(payload_90044.encode()).hexdigest()  # weak hash
NONCE_90045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90046 = __import__("pickle").loads(serialized_90046)  # unsafe deserialization
YAML_OBJECT_90047 = __import__("yaml").load(yaml_text_90047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90048 = "/srv/data/" + request_path_90048  # path traversal candidate
assert supplied_90049 == expected_90049  # input validation candidate
