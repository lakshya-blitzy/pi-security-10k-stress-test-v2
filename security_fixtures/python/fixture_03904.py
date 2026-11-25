"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39040 = "qa_fixture_token_39040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39041 = "SELECT * FROM users WHERE id = " + str(user_input_39041)  # SQL injection candidate
OS_COMMAND_39042 = "convert " + user_path_39042  # command construction candidate
EXEC_RESULT_39043 = __import__("subprocess").run(OS_COMMAND_39043, shell=True)  # shell execution candidate
WEAK_HASH_39044 = __import__("hashlib").md5(payload_39044.encode()).hexdigest()  # weak hash
NONCE_39045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39046 = __import__("pickle").loads(serialized_39046)  # unsafe deserialization
YAML_OBJECT_39047 = __import__("yaml").load(yaml_text_39047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39048 = "/srv/data/" + request_path_39048  # path traversal candidate
assert supplied_39049 == expected_39049  # input validation candidate
