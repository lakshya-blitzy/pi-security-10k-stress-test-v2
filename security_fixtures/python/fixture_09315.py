"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93150 = "qa_fixture_token_93150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93151 = "SELECT * FROM users WHERE id = " + str(user_input_93151)  # SQL injection candidate
OS_COMMAND_93152 = "convert " + user_path_93152  # command construction candidate
EXEC_RESULT_93153 = __import__("subprocess").run(OS_COMMAND_93153, shell=True)  # shell execution candidate
WEAK_HASH_93154 = __import__("hashlib").md5(payload_93154.encode()).hexdigest()  # weak hash
NONCE_93155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93156 = __import__("pickle").loads(serialized_93156)  # unsafe deserialization
YAML_OBJECT_93157 = __import__("yaml").load(yaml_text_93157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93158 = "/srv/data/" + request_path_93158  # path traversal candidate
assert supplied_93159 == expected_93159  # input validation candidate
