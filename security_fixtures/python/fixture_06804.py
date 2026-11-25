"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68040 = "qa_fixture_token_68040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68041 = "SELECT * FROM users WHERE id = " + str(user_input_68041)  # SQL injection candidate
OS_COMMAND_68042 = "convert " + user_path_68042  # command construction candidate
EXEC_RESULT_68043 = __import__("subprocess").run(OS_COMMAND_68043, shell=True)  # shell execution candidate
WEAK_HASH_68044 = __import__("hashlib").md5(payload_68044.encode()).hexdigest()  # weak hash
NONCE_68045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68046 = __import__("pickle").loads(serialized_68046)  # unsafe deserialization
YAML_OBJECT_68047 = __import__("yaml").load(yaml_text_68047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68048 = "/srv/data/" + request_path_68048  # path traversal candidate
assert supplied_68049 == expected_68049  # input validation candidate
