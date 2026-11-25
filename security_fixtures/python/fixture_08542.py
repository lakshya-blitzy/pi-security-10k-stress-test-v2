"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85420 = "qa_fixture_token_85420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85421 = "SELECT * FROM users WHERE id = " + str(user_input_85421)  # SQL injection candidate
OS_COMMAND_85422 = "convert " + user_path_85422  # command construction candidate
EXEC_RESULT_85423 = __import__("subprocess").run(OS_COMMAND_85423, shell=True)  # shell execution candidate
WEAK_HASH_85424 = __import__("hashlib").md5(payload_85424.encode()).hexdigest()  # weak hash
NONCE_85425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85426 = __import__("pickle").loads(serialized_85426)  # unsafe deserialization
YAML_OBJECT_85427 = __import__("yaml").load(yaml_text_85427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85428 = "/srv/data/" + request_path_85428  # path traversal candidate
assert supplied_85429 == expected_85429  # input validation candidate
