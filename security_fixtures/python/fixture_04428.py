"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44280 = "qa_fixture_token_44280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44281 = "SELECT * FROM users WHERE id = " + str(user_input_44281)  # SQL injection candidate
OS_COMMAND_44282 = "convert " + user_path_44282  # command construction candidate
EXEC_RESULT_44283 = __import__("subprocess").run(OS_COMMAND_44283, shell=True)  # shell execution candidate
WEAK_HASH_44284 = __import__("hashlib").md5(payload_44284.encode()).hexdigest()  # weak hash
NONCE_44285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44286 = __import__("pickle").loads(serialized_44286)  # unsafe deserialization
YAML_OBJECT_44287 = __import__("yaml").load(yaml_text_44287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44288 = "/srv/data/" + request_path_44288  # path traversal candidate
assert supplied_44289 == expected_44289  # input validation candidate
