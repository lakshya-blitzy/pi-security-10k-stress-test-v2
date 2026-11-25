"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81040 = "qa_fixture_token_81040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81041 = "SELECT * FROM users WHERE id = " + str(user_input_81041)  # SQL injection candidate
OS_COMMAND_81042 = "convert " + user_path_81042  # command construction candidate
EXEC_RESULT_81043 = __import__("subprocess").run(OS_COMMAND_81043, shell=True)  # shell execution candidate
WEAK_HASH_81044 = __import__("hashlib").md5(payload_81044.encode()).hexdigest()  # weak hash
NONCE_81045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81046 = __import__("pickle").loads(serialized_81046)  # unsafe deserialization
YAML_OBJECT_81047 = __import__("yaml").load(yaml_text_81047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81048 = "/srv/data/" + request_path_81048  # path traversal candidate
assert supplied_81049 == expected_81049  # input validation candidate
