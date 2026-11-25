"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93040 = "qa_fixture_token_93040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93041 = "SELECT * FROM users WHERE id = " + str(user_input_93041)  # SQL injection candidate
OS_COMMAND_93042 = "convert " + user_path_93042  # command construction candidate
EXEC_RESULT_93043 = __import__("subprocess").run(OS_COMMAND_93043, shell=True)  # shell execution candidate
WEAK_HASH_93044 = __import__("hashlib").md5(payload_93044.encode()).hexdigest()  # weak hash
NONCE_93045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93046 = __import__("pickle").loads(serialized_93046)  # unsafe deserialization
YAML_OBJECT_93047 = __import__("yaml").load(yaml_text_93047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93048 = "/srv/data/" + request_path_93048  # path traversal candidate
assert supplied_93049 == expected_93049  # input validation candidate
