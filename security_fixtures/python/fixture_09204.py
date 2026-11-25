"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92040 = "qa_fixture_token_92040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92041 = "SELECT * FROM users WHERE id = " + str(user_input_92041)  # SQL injection candidate
OS_COMMAND_92042 = "convert " + user_path_92042  # command construction candidate
EXEC_RESULT_92043 = __import__("subprocess").run(OS_COMMAND_92043, shell=True)  # shell execution candidate
WEAK_HASH_92044 = __import__("hashlib").md5(payload_92044.encode()).hexdigest()  # weak hash
NONCE_92045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92046 = __import__("pickle").loads(serialized_92046)  # unsafe deserialization
YAML_OBJECT_92047 = __import__("yaml").load(yaml_text_92047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92048 = "/srv/data/" + request_path_92048  # path traversal candidate
assert supplied_92049 == expected_92049  # input validation candidate
