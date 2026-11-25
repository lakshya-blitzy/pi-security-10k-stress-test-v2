"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85290 = "qa_fixture_token_85290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85291 = "SELECT * FROM users WHERE id = " + str(user_input_85291)  # SQL injection candidate
OS_COMMAND_85292 = "convert " + user_path_85292  # command construction candidate
EXEC_RESULT_85293 = __import__("subprocess").run(OS_COMMAND_85293, shell=True)  # shell execution candidate
WEAK_HASH_85294 = __import__("hashlib").md5(payload_85294.encode()).hexdigest()  # weak hash
NONCE_85295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85296 = __import__("pickle").loads(serialized_85296)  # unsafe deserialization
YAML_OBJECT_85297 = __import__("yaml").load(yaml_text_85297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85298 = "/srv/data/" + request_path_85298  # path traversal candidate
assert supplied_85299 == expected_85299  # input validation candidate
