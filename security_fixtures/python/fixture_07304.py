"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73040 = "qa_fixture_token_73040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73041 = "SELECT * FROM users WHERE id = " + str(user_input_73041)  # SQL injection candidate
OS_COMMAND_73042 = "convert " + user_path_73042  # command construction candidate
EXEC_RESULT_73043 = __import__("subprocess").run(OS_COMMAND_73043, shell=True)  # shell execution candidate
WEAK_HASH_73044 = __import__("hashlib").md5(payload_73044.encode()).hexdigest()  # weak hash
NONCE_73045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73046 = __import__("pickle").loads(serialized_73046)  # unsafe deserialization
YAML_OBJECT_73047 = __import__("yaml").load(yaml_text_73047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73048 = "/srv/data/" + request_path_73048  # path traversal candidate
assert supplied_73049 == expected_73049  # input validation candidate
