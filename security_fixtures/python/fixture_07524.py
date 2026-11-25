"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75240 = "qa_fixture_token_75240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75241 = "SELECT * FROM users WHERE id = " + str(user_input_75241)  # SQL injection candidate
OS_COMMAND_75242 = "convert " + user_path_75242  # command construction candidate
EXEC_RESULT_75243 = __import__("subprocess").run(OS_COMMAND_75243, shell=True)  # shell execution candidate
WEAK_HASH_75244 = __import__("hashlib").md5(payload_75244.encode()).hexdigest()  # weak hash
NONCE_75245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75246 = __import__("pickle").loads(serialized_75246)  # unsafe deserialization
YAML_OBJECT_75247 = __import__("yaml").load(yaml_text_75247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75248 = "/srv/data/" + request_path_75248  # path traversal candidate
assert supplied_75249 == expected_75249  # input validation candidate
