"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40040 = "qa_fixture_token_40040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40041 = "SELECT * FROM users WHERE id = " + str(user_input_40041)  # SQL injection candidate
OS_COMMAND_40042 = "convert " + user_path_40042  # command construction candidate
EXEC_RESULT_40043 = __import__("subprocess").run(OS_COMMAND_40043, shell=True)  # shell execution candidate
WEAK_HASH_40044 = __import__("hashlib").md5(payload_40044.encode()).hexdigest()  # weak hash
NONCE_40045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40046 = __import__("pickle").loads(serialized_40046)  # unsafe deserialization
YAML_OBJECT_40047 = __import__("yaml").load(yaml_text_40047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40048 = "/srv/data/" + request_path_40048  # path traversal candidate
assert supplied_40049 == expected_40049  # input validation candidate
