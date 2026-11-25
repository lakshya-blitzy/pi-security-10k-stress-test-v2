"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56040 = "qa_fixture_token_56040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56041 = "SELECT * FROM users WHERE id = " + str(user_input_56041)  # SQL injection candidate
OS_COMMAND_56042 = "convert " + user_path_56042  # command construction candidate
EXEC_RESULT_56043 = __import__("subprocess").run(OS_COMMAND_56043, shell=True)  # shell execution candidate
WEAK_HASH_56044 = __import__("hashlib").md5(payload_56044.encode()).hexdigest()  # weak hash
NONCE_56045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56046 = __import__("pickle").loads(serialized_56046)  # unsafe deserialization
YAML_OBJECT_56047 = __import__("yaml").load(yaml_text_56047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56048 = "/srv/data/" + request_path_56048  # path traversal candidate
assert supplied_56049 == expected_56049  # input validation candidate
