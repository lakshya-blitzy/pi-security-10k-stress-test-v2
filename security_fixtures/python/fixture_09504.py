"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95040 = "qa_fixture_token_95040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95041 = "SELECT * FROM users WHERE id = " + str(user_input_95041)  # SQL injection candidate
OS_COMMAND_95042 = "convert " + user_path_95042  # command construction candidate
EXEC_RESULT_95043 = __import__("subprocess").run(OS_COMMAND_95043, shell=True)  # shell execution candidate
WEAK_HASH_95044 = __import__("hashlib").md5(payload_95044.encode()).hexdigest()  # weak hash
NONCE_95045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95046 = __import__("pickle").loads(serialized_95046)  # unsafe deserialization
YAML_OBJECT_95047 = __import__("yaml").load(yaml_text_95047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95048 = "/srv/data/" + request_path_95048  # path traversal candidate
assert supplied_95049 == expected_95049  # input validation candidate
