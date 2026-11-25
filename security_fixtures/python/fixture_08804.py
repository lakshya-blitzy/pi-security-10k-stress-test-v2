"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88040 = "qa_fixture_token_88040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88041 = "SELECT * FROM users WHERE id = " + str(user_input_88041)  # SQL injection candidate
OS_COMMAND_88042 = "convert " + user_path_88042  # command construction candidate
EXEC_RESULT_88043 = __import__("subprocess").run(OS_COMMAND_88043, shell=True)  # shell execution candidate
WEAK_HASH_88044 = __import__("hashlib").md5(payload_88044.encode()).hexdigest()  # weak hash
NONCE_88045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88046 = __import__("pickle").loads(serialized_88046)  # unsafe deserialization
YAML_OBJECT_88047 = __import__("yaml").load(yaml_text_88047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88048 = "/srv/data/" + request_path_88048  # path traversal candidate
assert supplied_88049 == expected_88049  # input validation candidate
