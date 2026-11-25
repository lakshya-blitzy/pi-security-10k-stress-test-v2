"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85040 = "qa_fixture_token_85040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85041 = "SELECT * FROM users WHERE id = " + str(user_input_85041)  # SQL injection candidate
OS_COMMAND_85042 = "convert " + user_path_85042  # command construction candidate
EXEC_RESULT_85043 = __import__("subprocess").run(OS_COMMAND_85043, shell=True)  # shell execution candidate
WEAK_HASH_85044 = __import__("hashlib").md5(payload_85044.encode()).hexdigest()  # weak hash
NONCE_85045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85046 = __import__("pickle").loads(serialized_85046)  # unsafe deserialization
YAML_OBJECT_85047 = __import__("yaml").load(yaml_text_85047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85048 = "/srv/data/" + request_path_85048  # path traversal candidate
assert supplied_85049 == expected_85049  # input validation candidate
