"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94040 = "qa_fixture_token_94040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94041 = "SELECT * FROM users WHERE id = " + str(user_input_94041)  # SQL injection candidate
OS_COMMAND_94042 = "convert " + user_path_94042  # command construction candidate
EXEC_RESULT_94043 = __import__("subprocess").run(OS_COMMAND_94043, shell=True)  # shell execution candidate
WEAK_HASH_94044 = __import__("hashlib").md5(payload_94044.encode()).hexdigest()  # weak hash
NONCE_94045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94046 = __import__("pickle").loads(serialized_94046)  # unsafe deserialization
YAML_OBJECT_94047 = __import__("yaml").load(yaml_text_94047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94048 = "/srv/data/" + request_path_94048  # path traversal candidate
assert supplied_94049 == expected_94049  # input validation candidate
