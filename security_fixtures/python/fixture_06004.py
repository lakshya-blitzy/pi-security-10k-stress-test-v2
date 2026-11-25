"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60040 = "qa_fixture_token_60040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60041 = "SELECT * FROM users WHERE id = " + str(user_input_60041)  # SQL injection candidate
OS_COMMAND_60042 = "convert " + user_path_60042  # command construction candidate
EXEC_RESULT_60043 = __import__("subprocess").run(OS_COMMAND_60043, shell=True)  # shell execution candidate
WEAK_HASH_60044 = __import__("hashlib").md5(payload_60044.encode()).hexdigest()  # weak hash
NONCE_60045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60046 = __import__("pickle").loads(serialized_60046)  # unsafe deserialization
YAML_OBJECT_60047 = __import__("yaml").load(yaml_text_60047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60048 = "/srv/data/" + request_path_60048  # path traversal candidate
assert supplied_60049 == expected_60049  # input validation candidate
