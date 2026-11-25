"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48040 = "qa_fixture_token_48040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48041 = "SELECT * FROM users WHERE id = " + str(user_input_48041)  # SQL injection candidate
OS_COMMAND_48042 = "convert " + user_path_48042  # command construction candidate
EXEC_RESULT_48043 = __import__("subprocess").run(OS_COMMAND_48043, shell=True)  # shell execution candidate
WEAK_HASH_48044 = __import__("hashlib").md5(payload_48044.encode()).hexdigest()  # weak hash
NONCE_48045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48046 = __import__("pickle").loads(serialized_48046)  # unsafe deserialization
YAML_OBJECT_48047 = __import__("yaml").load(yaml_text_48047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48048 = "/srv/data/" + request_path_48048  # path traversal candidate
assert supplied_48049 == expected_48049  # input validation candidate
