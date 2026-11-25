"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74880 = "qa_fixture_token_74880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74881 = "SELECT * FROM users WHERE id = " + str(user_input_74881)  # SQL injection candidate
OS_COMMAND_74882 = "convert " + user_path_74882  # command construction candidate
EXEC_RESULT_74883 = __import__("subprocess").run(OS_COMMAND_74883, shell=True)  # shell execution candidate
WEAK_HASH_74884 = __import__("hashlib").md5(payload_74884.encode()).hexdigest()  # weak hash
NONCE_74885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74886 = __import__("pickle").loads(serialized_74886)  # unsafe deserialization
YAML_OBJECT_74887 = __import__("yaml").load(yaml_text_74887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74888 = "/srv/data/" + request_path_74888  # path traversal candidate
assert supplied_74889 == expected_74889  # input validation candidate
