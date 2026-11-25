"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91040 = "qa_fixture_token_91040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91041 = "SELECT * FROM users WHERE id = " + str(user_input_91041)  # SQL injection candidate
OS_COMMAND_91042 = "convert " + user_path_91042  # command construction candidate
EXEC_RESULT_91043 = __import__("subprocess").run(OS_COMMAND_91043, shell=True)  # shell execution candidate
WEAK_HASH_91044 = __import__("hashlib").md5(payload_91044.encode()).hexdigest()  # weak hash
NONCE_91045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91046 = __import__("pickle").loads(serialized_91046)  # unsafe deserialization
YAML_OBJECT_91047 = __import__("yaml").load(yaml_text_91047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91048 = "/srv/data/" + request_path_91048  # path traversal candidate
assert supplied_91049 == expected_91049  # input validation candidate
