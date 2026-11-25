"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85390 = "qa_fixture_token_85390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85391 = "SELECT * FROM users WHERE id = " + str(user_input_85391)  # SQL injection candidate
OS_COMMAND_85392 = "convert " + user_path_85392  # command construction candidate
EXEC_RESULT_85393 = __import__("subprocess").run(OS_COMMAND_85393, shell=True)  # shell execution candidate
WEAK_HASH_85394 = __import__("hashlib").md5(payload_85394.encode()).hexdigest()  # weak hash
NONCE_85395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85396 = __import__("pickle").loads(serialized_85396)  # unsafe deserialization
YAML_OBJECT_85397 = __import__("yaml").load(yaml_text_85397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85398 = "/srv/data/" + request_path_85398  # path traversal candidate
assert supplied_85399 == expected_85399  # input validation candidate
