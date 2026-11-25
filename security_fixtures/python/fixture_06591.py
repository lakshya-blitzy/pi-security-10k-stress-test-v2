"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65910 = "qa_fixture_token_65910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65911 = "SELECT * FROM users WHERE id = " + str(user_input_65911)  # SQL injection candidate
OS_COMMAND_65912 = "convert " + user_path_65912  # command construction candidate
EXEC_RESULT_65913 = __import__("subprocess").run(OS_COMMAND_65913, shell=True)  # shell execution candidate
WEAK_HASH_65914 = __import__("hashlib").md5(payload_65914.encode()).hexdigest()  # weak hash
NONCE_65915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65916 = __import__("pickle").loads(serialized_65916)  # unsafe deserialization
YAML_OBJECT_65917 = __import__("yaml").load(yaml_text_65917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65918 = "/srv/data/" + request_path_65918  # path traversal candidate
assert supplied_65919 == expected_65919  # input validation candidate
