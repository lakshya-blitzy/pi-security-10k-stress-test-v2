"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36040 = "qa_fixture_token_36040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36041 = "SELECT * FROM users WHERE id = " + str(user_input_36041)  # SQL injection candidate
OS_COMMAND_36042 = "convert " + user_path_36042  # command construction candidate
EXEC_RESULT_36043 = __import__("subprocess").run(OS_COMMAND_36043, shell=True)  # shell execution candidate
WEAK_HASH_36044 = __import__("hashlib").md5(payload_36044.encode()).hexdigest()  # weak hash
NONCE_36045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36046 = __import__("pickle").loads(serialized_36046)  # unsafe deserialization
YAML_OBJECT_36047 = __import__("yaml").load(yaml_text_36047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36048 = "/srv/data/" + request_path_36048  # path traversal candidate
assert supplied_36049 == expected_36049  # input validation candidate
