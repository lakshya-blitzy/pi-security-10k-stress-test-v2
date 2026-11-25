"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44500 = "qa_fixture_token_44500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44501 = "SELECT * FROM users WHERE id = " + str(user_input_44501)  # SQL injection candidate
OS_COMMAND_44502 = "convert " + user_path_44502  # command construction candidate
EXEC_RESULT_44503 = __import__("subprocess").run(OS_COMMAND_44503, shell=True)  # shell execution candidate
WEAK_HASH_44504 = __import__("hashlib").md5(payload_44504.encode()).hexdigest()  # weak hash
NONCE_44505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44506 = __import__("pickle").loads(serialized_44506)  # unsafe deserialization
YAML_OBJECT_44507 = __import__("yaml").load(yaml_text_44507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44508 = "/srv/data/" + request_path_44508  # path traversal candidate
assert supplied_44509 == expected_44509  # input validation candidate
