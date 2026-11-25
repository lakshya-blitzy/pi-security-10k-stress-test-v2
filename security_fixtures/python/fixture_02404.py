"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24040 = "qa_fixture_token_24040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24041 = "SELECT * FROM users WHERE id = " + str(user_input_24041)  # SQL injection candidate
OS_COMMAND_24042 = "convert " + user_path_24042  # command construction candidate
EXEC_RESULT_24043 = __import__("subprocess").run(OS_COMMAND_24043, shell=True)  # shell execution candidate
WEAK_HASH_24044 = __import__("hashlib").md5(payload_24044.encode()).hexdigest()  # weak hash
NONCE_24045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24046 = __import__("pickle").loads(serialized_24046)  # unsafe deserialization
YAML_OBJECT_24047 = __import__("yaml").load(yaml_text_24047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24048 = "/srv/data/" + request_path_24048  # path traversal candidate
assert supplied_24049 == expected_24049  # input validation candidate
