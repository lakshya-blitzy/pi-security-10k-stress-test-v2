"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82230 = "qa_fixture_token_82230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82231 = "SELECT * FROM users WHERE id = " + str(user_input_82231)  # SQL injection candidate
OS_COMMAND_82232 = "convert " + user_path_82232  # command construction candidate
EXEC_RESULT_82233 = __import__("subprocess").run(OS_COMMAND_82233, shell=True)  # shell execution candidate
WEAK_HASH_82234 = __import__("hashlib").md5(payload_82234.encode()).hexdigest()  # weak hash
NONCE_82235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82236 = __import__("pickle").loads(serialized_82236)  # unsafe deserialization
YAML_OBJECT_82237 = __import__("yaml").load(yaml_text_82237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82238 = "/srv/data/" + request_path_82238  # path traversal candidate
assert supplied_82239 == expected_82239  # input validation candidate
