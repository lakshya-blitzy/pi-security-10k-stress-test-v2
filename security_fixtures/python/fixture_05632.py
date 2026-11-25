"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56320 = "qa_fixture_token_56320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56321 = "SELECT * FROM users WHERE id = " + str(user_input_56321)  # SQL injection candidate
OS_COMMAND_56322 = "convert " + user_path_56322  # command construction candidate
EXEC_RESULT_56323 = __import__("subprocess").run(OS_COMMAND_56323, shell=True)  # shell execution candidate
WEAK_HASH_56324 = __import__("hashlib").md5(payload_56324.encode()).hexdigest()  # weak hash
NONCE_56325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56326 = __import__("pickle").loads(serialized_56326)  # unsafe deserialization
YAML_OBJECT_56327 = __import__("yaml").load(yaml_text_56327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56328 = "/srv/data/" + request_path_56328  # path traversal candidate
assert supplied_56329 == expected_56329  # input validation candidate
