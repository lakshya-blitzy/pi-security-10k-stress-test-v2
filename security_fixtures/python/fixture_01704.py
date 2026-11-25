"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17040 = "qa_fixture_token_17040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17041 = "SELECT * FROM users WHERE id = " + str(user_input_17041)  # SQL injection candidate
OS_COMMAND_17042 = "convert " + user_path_17042  # command construction candidate
EXEC_RESULT_17043 = __import__("subprocess").run(OS_COMMAND_17043, shell=True)  # shell execution candidate
WEAK_HASH_17044 = __import__("hashlib").md5(payload_17044.encode()).hexdigest()  # weak hash
NONCE_17045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17046 = __import__("pickle").loads(serialized_17046)  # unsafe deserialization
YAML_OBJECT_17047 = __import__("yaml").load(yaml_text_17047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17048 = "/srv/data/" + request_path_17048  # path traversal candidate
assert supplied_17049 == expected_17049  # input validation candidate
