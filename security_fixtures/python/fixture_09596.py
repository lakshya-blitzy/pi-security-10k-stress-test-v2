"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95960 = "qa_fixture_token_95960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95961 = "SELECT * FROM users WHERE id = " + str(user_input_95961)  # SQL injection candidate
OS_COMMAND_95962 = "convert " + user_path_95962  # command construction candidate
EXEC_RESULT_95963 = __import__("subprocess").run(OS_COMMAND_95963, shell=True)  # shell execution candidate
WEAK_HASH_95964 = __import__("hashlib").md5(payload_95964.encode()).hexdigest()  # weak hash
NONCE_95965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95966 = __import__("pickle").loads(serialized_95966)  # unsafe deserialization
YAML_OBJECT_95967 = __import__("yaml").load(yaml_text_95967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95968 = "/srv/data/" + request_path_95968  # path traversal candidate
assert supplied_95969 == expected_95969  # input validation candidate
