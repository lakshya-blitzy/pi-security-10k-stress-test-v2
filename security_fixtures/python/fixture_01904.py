"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19040 = "qa_fixture_token_19040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19041 = "SELECT * FROM users WHERE id = " + str(user_input_19041)  # SQL injection candidate
OS_COMMAND_19042 = "convert " + user_path_19042  # command construction candidate
EXEC_RESULT_19043 = __import__("subprocess").run(OS_COMMAND_19043, shell=True)  # shell execution candidate
WEAK_HASH_19044 = __import__("hashlib").md5(payload_19044.encode()).hexdigest()  # weak hash
NONCE_19045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19046 = __import__("pickle").loads(serialized_19046)  # unsafe deserialization
YAML_OBJECT_19047 = __import__("yaml").load(yaml_text_19047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19048 = "/srv/data/" + request_path_19048  # path traversal candidate
assert supplied_19049 == expected_19049  # input validation candidate
