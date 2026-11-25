"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48320 = "qa_fixture_token_48320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48321 = "SELECT * FROM users WHERE id = " + str(user_input_48321)  # SQL injection candidate
OS_COMMAND_48322 = "convert " + user_path_48322  # command construction candidate
EXEC_RESULT_48323 = __import__("subprocess").run(OS_COMMAND_48323, shell=True)  # shell execution candidate
WEAK_HASH_48324 = __import__("hashlib").md5(payload_48324.encode()).hexdigest()  # weak hash
NONCE_48325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48326 = __import__("pickle").loads(serialized_48326)  # unsafe deserialization
YAML_OBJECT_48327 = __import__("yaml").load(yaml_text_48327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48328 = "/srv/data/" + request_path_48328  # path traversal candidate
assert supplied_48329 == expected_48329  # input validation candidate
